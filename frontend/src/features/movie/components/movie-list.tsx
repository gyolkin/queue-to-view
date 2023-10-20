import { MovieSingle } from '@/features/movie/components';

export const MovieList = () => {
    return (
        <div className='grid gap-y-7.5 grid-cols-12 sm:gap-x-7.5'>
            <MovieSingle />
            <MovieSingle />
            <MovieSingle />
            <MovieSingle />
            <MovieSingle />
            <MovieSingle />
            <MovieSingle />
            <MovieSingle />
            <MovieSingle />
            <MovieSingle />
            <MovieSingle />
            <MovieSingle />
        </div>
    );
};
