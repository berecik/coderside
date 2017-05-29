/**
 * Created by beret on 03.05.17.
 */
import React from 'react';
import './ToggleButton.scss';

export default class ToggleButton extends React.Component {
    constructor() {
        super();

        let on = false;
        if(this.props && this.props.on){
            on = this.props.on
        }

        this.state = {on: on}
    }

    onToggleClick(event) {
        event.preventDefault();
        this.setState({
                on: !this.state.on
            },
            () => this.props.onChange ? this.props.onChange(this.state.on) : null
        );
    }

    render() {
        return (
            <a
                className="toggle-button"
                href="#"
                onClick={this.onToggleClick.bind(this)}
            >
                <span
                    className={`${this.state.on ? "toggle-on" : "toggle-off"}`}
                >
                    <div></div>
                </span>
            </a>
        );
    }
}