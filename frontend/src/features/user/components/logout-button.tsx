import { Button } from '@/components';
import { textMap } from '@/constants';
import { authApi, useLogoutMutation } from '@/features/user';
import { useAppDispatch } from '@/hooks/store';

export const LogoutButton = () => {
    const { user } = textMap.navbar;
    const dispatch = useAppDispatch();
    const [logout] = useLogoutMutation();
    const handleSubmit = async () => {
        await logout().unwrap();
        dispatch(authApi.util.resetApiState());
    };
    return (
        <Button shape='link' variant='link' onClick={handleSubmit}>
            {user.logout}
        </Button>
    );
};
