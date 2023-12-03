import { PropsWithChildren } from 'react';

import { skipToken } from '@reduxjs/toolkit/query';
import Cookies from 'js-cookie';

import { configMap } from '@/constants';
import { useMeQuery } from '@/features/user';

export const ApplicationWrapper = ({ children }: PropsWithChildren) => {
    const { name: cookie_name } = configMap.auth_cookie;
    const { isLoading } = useMeQuery(
        Cookies.get(cookie_name) ? undefined : skipToken,
    );
    // todo: сделать нормальную обработку загрузки и ошибок
    if (isLoading) {
        return <div>Loading...</div>;
    }
    return children;
};
