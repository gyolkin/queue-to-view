import Cookies from 'js-cookie';

import { Button } from '@/components';
import { configMap, textMap } from '@/constants';
import { authApi, useLogoutMutation } from '@/features/user';
import { useAppDispatch } from '@/hooks/store';

export const LogoutButton = () => {
    const { user } = textMap.navbar;
    const { name: cookie_name } = configMap.auth_cookie;
    const dispatch = useAppDispatch();
    const [logout] = useLogoutMutation();
    const handleSubmit = async () => {
        await logout().unwrap();
        Cookies.remove(cookie_name);
        dispatch(authApi.util.resetApiState());
    };
    return (
        <Button shape='link' variant='link' onClick={handleSubmit}>
            {user.logout}
        </Button>
    );
};
