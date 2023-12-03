import './base.css';

import React from 'react';

import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import { BrowserRouter } from 'react-router-dom';

import { Router } from '@/core/router';
import { store } from '@/core/store';
import { ApplicationWrapper } from '@/core/wrapper';

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <Provider store={store}>
            <BrowserRouter>
                <ApplicationWrapper>
                    <Router />
                </ApplicationWrapper>
            </BrowserRouter>
        </Provider>
    </React.StrictMode>,
);
