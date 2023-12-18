import type { ReadGenre } from '@/features/genre';

interface Movie {
    title: string;
    description: string;
    release_year: number;
    imdb_rating?: number;
    duration: number;
    country: string;
    genres: Array<number>;
    poster: string;
}

export interface ReadMovie extends Readonly<Omit<Movie, 'genres'>> {
    readonly id: number;
    readonly slug: string;
    readonly created_at: string;
    readonly genres: Array<ReadGenre>;
    readonly is_watched: boolean;
}
