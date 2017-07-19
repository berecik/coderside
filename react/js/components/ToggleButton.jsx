/**
 * Created by beret on 03.05.17.
 */
import React from 'react';
import './ToggleButton.scss';

export default class ToggleButton extends React.Component {
    constructor(props) {
        super(props);

        let on = false;

        if(this.props.on){
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
            <span
                className="toggle-button"
                onClick={this.onToggleClick.bind(this)}
            >
                <span
                    className={`${this.state.on ? "toggle-on" : "toggle-off"}`}
                >
                    <span></span>
                </span>
            </span>
        );
    }
}