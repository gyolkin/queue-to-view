import { Outlet } from 'react-router-dom';

import { Header } from '@/components';
import { cn } from '@/utils/helpers';

interface BasicLayoutProps {
    includeHeader?: boolean;
}

export const BasicLayout = ({ includeHeader = false }: BasicLayoutProps) => {
    return (
        <div id='site-wrapper' className='flex flex-col h-full'>
            {includeHeader && <Header />}
            <main
                className={cn(
                    includeHeader
                        ? 'container mx-auto pt-4 md:pt-6'
                        : 'container flex justify-center items-center pt-20 lg:pt-0 lg:h-screen',
                )}
            >
                <Outlet />
            </main>
        </div>
    );
};
