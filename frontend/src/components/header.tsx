import { NavbarLink, DefaultLink, Logo } from '@/components';
import { routerMap, textMap } from '@/constants';
import { NavbarUser } from '@/features/user/components';

export const Header = () => {
    return (
        <header className='container'>
            <nav className='flex h-16 items-center gap-x-3 lg:gap-x-6 py-1 lg:h-20 lg:py-4'>
                <div className='shrink-0'>
                    <Logo tiny />
                </div>
                <ul className='flex gap-x-0 xl:gap-x-3 text-sm font-bold text-white'>
                    <li>
                        <NavbarLink to={routerMap.home}>
                            {textMap.navbar.home}
                        </NavbarLink>
                    </li>
                    <li className='relative [&>.sub-menu]:hover:visible [&>.sub-menu]:hover:animate-popper-pop-in [&>.sub-menu]:hover:opacity-100'>
                        <DefaultLink variant='dropdown' to='#'>
                            {textMap.navbar.genres}
                        </DefaultLink>
                        <ul className='sub-menu invisible absolute z-20 flex w-40 flex-col bg-gray-700 py-2.5 text-sm font-bold opacity-0 shadow-2xl transition-all'>
                            <li className='px-5'>
                                <DefaultLink to='/genre-1'>
                                    Genre #1
                                </DefaultLink>
                            </li>
                            <li className='px-5'>
                                <DefaultLink to='/genre-2'>
                                    Genre #2
                                </DefaultLink>
                            </li>
                        </ul>
                    </li>
                </ul>
                <ul className='flex ml-auto text-sm font-bold text-white'>
                    <NavbarUser />
                </ul>
            </nav>
        </header>
    );
};
