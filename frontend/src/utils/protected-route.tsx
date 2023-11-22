import { Navigate } from 'react-router-dom';

import { routerMap } from '@/constants';
import { selectIsAuthenticated } from '@/features/user';
import { useAppSelector } from '@/hooks/store';

interface ProtectedRouteProps extends React.PropsWithChildren {
    anonymous?: boolean;
}

export const ProtectedRoute: React.FC<ProtectedRouteProps> = ({
    children,
    anonymous = false,
}) => {
    const isAuthenticated = useAppSelector(selectIsAuthenticated);
    if (anonymous && isAuthenticated) {
        return <Navigate to={routerMap.home} />;
    }
    if (!anonymous && !isAuthenticated) {
        return <Navigate to={routerMap.sign_in} />;
    }
    return children;
};
