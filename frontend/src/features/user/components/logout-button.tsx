import { Button } from '@/components';
import { textMap } from '@/constants';
import { useLogoutMutation } from '@/features/user';

export const LogoutButton = () => {
    const { user } = textMap.navbar;
    const [logout] = useLogoutMutation();
    const handleSubmit = async () => {
        await logout().unwrap();
    };
    return (
        <Button shape='link' variant='link' onClick={handleSubmit}>
            {user.logout}
        </Button>
    );
};
