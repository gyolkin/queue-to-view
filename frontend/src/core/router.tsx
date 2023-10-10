import { Routes, Route } from 'react-router-dom';

import { HomePage } from '@/pages/home';

export const Router = () => {
    return (
        <>
            <Routes>
                <Route path='/' element={<HomePage />} />
            </Routes>
        </>
    );
};
