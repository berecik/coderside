/**
 * Created by beret on 29.05.17.
 */

import React from 'react';
import ReactDOM from 'react-dom';

import CodeEditor from './components/CodeEditor.jsx';

document.addEventListener('DOMContentLoaded', function () {

    ReactDOM.render(
        <div>
            <h1>Code Editor!</h1>
            <CodeEditor/>
        </div>,
        document.getElementById('react-root')
    );
});