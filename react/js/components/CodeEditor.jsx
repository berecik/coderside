/**
 * Created by beret on 03.05.17.
 */
import React from 'react';
import CodeMirror from 'react-codemirror';
import 'codemirror/lib/codemirror.css';
import ToggleButton from './ToggleButton.jsx';
import 'codemirror/mode/python/python';
import 'codemirror/mode/javascript/javascript';
import 'codemirror/mode/xml/xml';
import 'codemirror/mode/markdown/markdown'
import './md5';


function HelloAllMyNameIsLongerThanYour() {
    return <h1>Hello<ToggleButton/></h1>;
}


export default class CodeEditor extends React.Component {
    constructor(props) {
        super(props);
        let snippet = document.getElementById('source').value;
        this.state = {
            code: snippet,
            mode: 'python',
            edit: true,
            lineNumbers: true
        };
    }

    updateCode = newCode => {
        this.setState({
            code: newCode
        });
        document.getElementById('source').value = newCode;
        let hash = md5(newCode);
        console.log(hash);
    };

    copyText = () => {
        let text = this.state.code;
        if (window.clipboardData && window.clipboardData.setData) {
            // IE specific code path to prevent textarea being shown while dialog is visible.
            return clipboardData.setData("Text", text);

        } else if (document.queryCommandSupported && document.queryCommandSupported("copy")) {
            var textarea = document.createElement("textarea");
            textarea.textContent = text;
            textarea.style.position = "fixed";  // Prevent scrolling to bottom of page in MS Edge.
            document.body.appendChild(textarea);
            textarea.select();
            try {
                return document.execCommand("copy");  // Security exception may be thrown by some browsers.
            } catch (ex) {
                console.warn("Copy to clipboard failed.", ex);
                return false;
            } finally {
                document.body.removeChild(textarea);
            }
        }
    };

    changeEdit = (editState) => {
        this.setState({
            edit: editState
        });
    };

    changeLineNumbers = (lineNumbers) => {
        this.setState({
            lineNumbers: lineNumbers
        });
    };

    render() {
        let options = {
            lineNumbers: this.state.lineNumbers,
            readOnly: !this.state.edit,
            mode: 'python'
        };
        return <div>
            <HelloAllMyNameIsLongerThanYour/>
            <span>Edit:
                <ToggleButton on={this.state.edit} onChange={this.changeEdit}/>
            </span>
            <button onClick={this.copyText}>Copy</button>
            <button name="exec" value={true}>Execute</button>
            <button name="save" value={true}>Save</button>
            <input type="hidden" value={this.state.edit} name="edit"/>
            <CodeMirror
                ref="editor"
                value={this.state.code}
                onChange={this.updateCode}
                options={options}
                autoFocus={true}
            />
            <span>Line Numbers:
                <ToggleButton on={this.state.lineNumbers} onChange={this.changeLineNumbers}/>
            </span>
        </div>
    }
}