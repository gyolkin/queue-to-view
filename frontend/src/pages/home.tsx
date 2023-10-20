import { Heading } from '@/components';
import { textMap } from '@/constants';
import { RandomMovie, MovieList } from '@/features/movie/components';

export const HomePage = () => {
    const { home } = textMap.pages;
    return (
        <>
            <section className='pb-12 pt-4 md:pb-16 lg:pb-[100px] lg:pt-6'>
                <div className='container'>
                    <RandomMovie />
                </div>
            </section>
            <section className='pb-20 md:pb-24 lg:pb-[120px]'>
                <div className='container'>
                    <div className='mb-10 md:mb-12 lg:mb-16 xl:mb-20'>
                        <Heading>{home.best_films}</Heading>
                    </div>
                    <MovieList />
                </div>
            </section>
        </>
    );
};
