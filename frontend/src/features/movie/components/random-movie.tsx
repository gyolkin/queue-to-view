import bannerBg from '@/assets/banner-bg.jpg';
import bannerHero from '@/assets/banner-hero.png';
import { Button, DefaultLink, Heading } from '@/components';
import { routerMap } from '@/constants';
import { textMap } from '@/constants';
import { movieApi } from '@/features/movie';

export const RandomMovie = () => {
    const { random_movie: texts } = textMap.features;
    const [trigger, { data: movie, isLoading }] =
        movieApi.endpoints.randomMovie.useLazyQuery();

    return (
        <div className='mx-auto max-w-[1360px] px-5 md:pt-20 md:pb-5'>
            <div
                className='relative min-h-[220px] bg-cover bg-no-repeat'
                style={{ backgroundImage: `url(${bannerBg})` }}
            >
                <div className='container relative z-10 text-white'>
                    <div className='grid grid-cols-12 gap-x-5 gap-y-8 py-7 px-2 md:gap-x-6 lg:gap-y-12 lg:gap-x-7.5 lg:py-11 lg:px-0'>
                        <div className='col-span-full md:col-span-5 md:col-start-3 xl:-ml-7.5'>
                            <p className='text-lg font-bold'>
                                {texts.banner_smalltext}
                            </p>
                            <Heading size='md'>{texts.banner_heading}</Heading>
                            <p className='text-base font-medium leading-normal'>
                                {texts.banner_text}
                            </p>
                        </div>
                        <div className='col-span-full flex flex-wrap items-center justify-center gap-y-4 self-center md:col-span-4 md:col-start-9 lg:gap-y-0'>
                            <Button
                                onClick={() => trigger()}
                                disabled={isLoading}
                            >
                                {movie
                                    ? texts.button_next_trigger
                                    : texts.button_first_trigger}
                            </Button>
                        </div>
                    </div>
                </div>
                <div className='absolute inset-0 z-[1] bg-black mix-blend-color'></div>
                <div className='absolute inset-0 z-[2] bg-primary mix-blend-multiply'></div>
                <div className='absolute inset-0 z-[3] bg-gray-900 mix-blend-screen'></div>
                <img
                    className='pointer-events-none absolute -left-8 bottom-0 z-[4] hidden md:block'
                    src={bannerHero}
                    alt='Random Banner Hero'
                />
            </div>
            {movie && (
                <article className='flex flex-row flex-nowrap gap-x-2 max-w-2xl mx-auto pt-2'>
                    <img
                        className='aspect-[3/4] w-1/2 md:w-1/3'
                        src={movie.poster}
                        alt={movie.title}
                    />
                    <div className='flex flex-col'>
                        <Heading size='md'>
                            <DefaultLink
                                to={routerMap.movie + '/' + movie.slug}
                                className='py-0'
                            >
                                {movie.title}
                            </DefaultLink>
                        </Heading>
                        {movie.imdb_rating && (
                            <p className='text-accent font-bold'>
                                IMDB: {movie.imdb_rating}
                            </p>
                        )}
                        <div className='mb-4 text-ellipsis line-clamp-6'>
                            {movie.description}
                        </div>
                        <footer className='mt-auto'>
                            <DefaultLink
                                to={routerMap.movie + '/' + movie.slug}
                                className='text-white py-0'
                            >
                                {texts.film_details_link}
                            </DefaultLink>
                        </footer>
                    </div>
                </article>
            )}
        </div>
    );
};
