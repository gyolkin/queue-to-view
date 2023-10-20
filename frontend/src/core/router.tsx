import { Routes, Route } from 'react-router-dom';

import { BasicLayout } from '@/components';
import { routerMap } from '@/constants';
import { HomePage, NotFoundPage, LoginPage, RegisterPage } from '@/pages';

export const Router = () => {
    return (
        <>
            <Routes>
                <Route element={<BasicLayout includeHeader />}>
                    <Route path={routerMap.home} element={<HomePage />} />
                    <Route path={routerMap.sign_in} element={<LoginPage />} />
                    <Route
                        path={routerMap.sign_up}
                        element={<RegisterPage />}
                    />
                </Route>
                <Route element={<BasicLayout />}>
                    <Route path='*' element={<NotFoundPage />} />
                </Route>
            </Routes>
        </>
    );
};
