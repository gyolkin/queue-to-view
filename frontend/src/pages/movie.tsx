import { skipToken } from '@reduxjs/toolkit/query';
import { useParams } from 'react-router-dom';

import { useSingleMovieQuery } from '@/features/movie';
import { MovieDetails } from '@/features/movie/components';

export const MoviePage = () => {
    const { movieSlug } = useParams();
    const {
        data: movie,
        isLoading,
        error,
        isError,
    } = useSingleMovieQuery(movieSlug ? movieSlug : skipToken);

    if (!movie && isError && error) {
        return <div>Error</div>;
    }
    if (!movie || isLoading) {
        return <div>Loading...</div>;
    }
    return <MovieDetails movie={movie} />;
};
