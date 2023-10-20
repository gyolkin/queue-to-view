import { Heading, DefaultLink } from '@/components';
import { routerMap, textMap } from '@/constants';

export const NotFoundPage = () => {
    const { not_found } = textMap.pages;
    return (
        <div className='flex flex-col text-center gap-2 lg:gap-4'>
            <Heading size='xl'>{not_found.title}</Heading>
            <p>{not_found.desc}</p>
            <DefaultLink to={routerMap.home} variant='link'>
                {not_found.button_go_home}
            </DefaultLink>
        </div>
    );
};
