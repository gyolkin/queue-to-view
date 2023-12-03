import { Routes, Route } from 'react-router-dom';

import { BasicLayout } from '@/components';
import { routerMap } from '@/constants';
import {
    HomePage,
    NotFoundPage,
    LoginPage,
    RegisterPage,
    ProfilePage,
    MoviePage,
} from '@/pages';
import { ProtectedRoute } from '@/utils/protected-route';

export const Router = () => {
    return (
        <>
            <Routes>
                <Route element={<BasicLayout includeHeader />}>
                    <Route path={routerMap.home} element={<HomePage />} />
                    <Route
                        path={routerMap.sign_in}
                        element={
                            <ProtectedRoute anonymous>
                                <LoginPage />
                            </ProtectedRoute>
                        }
                    />
                    <Route
                        path={routerMap.sign_up}
                        element={
                            <ProtectedRoute anonymous>
                                <RegisterPage />
                            </ProtectedRoute>
                        }
                    />
                    <Route
                        path={routerMap.profile}
                        element={
                            <ProtectedRoute>
                                <ProfilePage />
                            </ProtectedRoute>
                        }
                    />
                    <Route
                        path={`${routerMap.movie}/:movieSlug`}
                        element={<MoviePage />}
                    />
                </Route>
                <Route element={<BasicLayout />}>
                    <Route path='*' element={<NotFoundPage />} />
                </Route>
            </Routes>
        </>
    );
};
