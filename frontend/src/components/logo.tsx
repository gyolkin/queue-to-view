import { Link } from 'react-router-dom';

import defaultLogo from '@/assets/qtv-small.png';
import tinyLogo from '@/assets/qtv-tiny.png';
import { routerMap } from '@/constants';

export const Logo = ({ tiny = false }: { tiny?: boolean }) => {
    if (tiny) {
        return (
            <Link to={routerMap.home}>
                <img src={tinyLogo} alt='Logo' />
            </Link>
        );
    }
    return (
        <Link to={routerMap.home}>
            <img src={defaultLogo} alt='Logo' />
        </Link>
    );
};
