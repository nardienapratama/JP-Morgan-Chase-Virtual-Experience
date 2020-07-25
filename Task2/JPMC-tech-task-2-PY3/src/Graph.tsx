import { Table } from '@jpmorganchase/perspective';
import { ServerRespond } from './DataStreamer';
import './Graph.css';
import { Component } from 'react';
import React from 'react';

/**
 * Props declaration for <Graph />
 */
interface IProps {
  data: ServerRespond[],
}

/**
 * Perspective library adds load to HTMLElement prototype.
 * This interface acts as a wrapper for Typescript compiler.
 */
interface PerspectiveViewerElement extends HTMLElement {
  load: (table: Table) => void,
}

/**
 * React component that renders Perspective based on data
 * parsed from its parent through data property.
 */
class Graph extends Component<IProps, {}> {
  // Perspective table
  table: Table | undefined;

  render() {
    return React.createElement('perspective-viewer');
  }

  componentDidMount() {
    // Get element to attach the table from the DOM.
    // PerspectiveViewerElement is removed from elem's data type since we've extended it as an HTMLElement
    const elem = document.getElementsByTagName('perspective-viewer')[0] as unknown as PerspectiveViewerElement;

    const schema = {
      stock: 'string',
      top_ask_price: 'float',
      top_bid_price: 'float',
      timestamp: 'date',
    };

    if (window.perspective && window.perspective.worker()) {
      this.table = window.perspective.worker().table(schema);
    }
    if (this.table) {
      // Load the `table` in the `<perspective-viewer>` DOM reference.

      // Add more Perspective configurations here.
      elem.load(this.table);
      // this part makes the graph
      elem.setAttribute('view', 'y_line');
      //this makes the two different colored lines on the graph ('ABC' and 'DEF')
      elem.setAttribute('column-pivots', '["stock"]');
      // this makes the labels for the x-axis
      elem.setAttribute('row-pivots', '["timestamp"]');
      // this makes the labels for the y-axis
      elem.setAttribute('columns', '["top_ask_price"]');
      // this makes sure that stocks and timestamps are distinct
      // and that if there are duplicates, top_ask_prices and top_bid_prices
      // will be averaged out
      elem.setAttribute('aggregates',  `
        {"stock": "distinct count",
        "top_ask_price": "avg",
        "top_bid_price": "avg",
        "timestamp": "distinct count"}`);
    }
  }

  componentDidUpdate() {
    // Everytime the data props is updated, insert the data into Perspective table
    if (this.table) {
      // As part of the task, you need to fix the way we update the data props to
      // avoid inserting duplicated entries into Perspective table again.
      this.table.update(this.props.data.map((el: any) => {
        // Format the data from ServerRespond to the schema
        return {
          stock: el.stock,
          top_ask_price: el.top_ask && el.top_ask.price || 0,
          top_bid_price: el.top_bid && el.top_bid.price || 0,
          timestamp: el.timestamp,
        };
      }));
    }
  }
}

export default Graph;
