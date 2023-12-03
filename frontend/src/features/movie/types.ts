import type { ReadCountry } from '@/features/country';
import type { ReadGenre } from '@/features/genre';

interface Movie {
    title: string;
    description: string;
    release_year: number;
    imdb_rating?: number;
    duration: number;
    country_id: number;
    genres: Array<number>;
    poster: string;
}

export interface ReadMovie
    extends Readonly<Omit<Movie, 'country_id' | 'genres'>> {
    readonly id: number;
    readonly slug: string;
    readonly created_at: string;
    readonly country: ReadCountry;
    readonly genres: Array<ReadGenre>;
}
