import { useAllMoviesQuery } from '@/features/movie';
import { MovieSingle } from '@/features/movie/components';

export const MovieList = () => {
    const { data, isLoading, error, isError } = useAllMoviesQuery();

    if (!data && isError && error) {
        return <div>Error</div>;
    }
    if (!data || data.length < 1 || isLoading) {
        return <div>Loading...</div>;
    }
    return (
        <div className='grid gap-y-7.5 grid-cols-12 sm:gap-x-7.5'>
            {data.map((item) => (
                <MovieSingle key={item.id} movie={item} />
            ))}
        </div>
    );
};
