import { DefaultLink } from '@/components';
import { routerMap, textMap } from '@/constants';
import { selectIsAuthenticated } from '@/features/user';
import { LogoutButton } from '@/features/user/components';
import { useAppSelector } from '@/hooks/store';

export const NavbarUser = () => {
    const { user } = textMap.navbar;
    const isAuthenticated = useAppSelector(selectIsAuthenticated);
    return (
        <li className='relative [&>.sub-menu]:hover:visible [&>.sub-menu]:hover:animate-popper-pop-in [&>.sub-menu]:hover:opacity-100'>
            <DefaultLink variant='dropdown' to='#'>
                {user.main_link}
            </DefaultLink>
            <ul className='sub-menu invisible absolute z-20 flex w-40 flex-col bg-gray-700 py-2.5 text-sm font-bold opacity-0 shadow-2xl transition-all'>
                {isAuthenticated ? (
                    <>
                        <li className='px-5'>
                            <DefaultLink to={routerMap.profile}>
                                {user.profile}
                            </DefaultLink>
                        </li>
                        <li className='px-5'>
                            <LogoutButton />
                        </li>
                    </>
                ) : (
                    <>
                        <li className='px-5'>
                            <DefaultLink to={routerMap.sign_in}>
                                {user.sign_in}
                            </DefaultLink>
                        </li>
                        <li className='px-5'>
                            <DefaultLink to={routerMap.sign_up}>
                                {user.sign_up}
                            </DefaultLink>
                        </li>
                    </>
                )}
            </ul>
        </li>
    );
};
