import { Star, Timer } from 'lucide-react';
import { Link } from 'react-router-dom';

import { Badge } from '@/components';
import { routerMap } from '@/constants';
import { joinGenres, type ReadMovie } from '@/features/movie';
import { WatchlistButton } from '@/features/watchlist/components'

export const MovieSingle = ({ movie }: { movie: ReadMovie }) => {
    return (
        <div className='col-span-full sm:col-span-6 lg:col-span-4 xl:col-span-3'>
            <figure className='mb-5'>
                <Link
                    className='group relative block h-full overflow-hidden bg-gray-900'
                    to={routerMap.movie + '/' + movie.slug}
                >
                    <img
                        className='aspect-[16/9] lg:aspect-[3/4] w-full object-cover transition-all duration-300 group-hover:scale-110 group-hover:opacity-75'
                        src={movie.poster}
                        alt={movie.title}
                    />
                    <div className='absolute inset-0 bg-black/60'></div>
                    <div className='absolute inline-flex gap-1 left-3.5 top-3'>
                        <Badge variant='primary' Icon={Timer}>
                            {movie.duration}
                        </Badge>
                        {movie.imdb_rating && (
                            <Badge variant='info' Icon={Star}>
                                {movie.imdb_rating}
                            </Badge>
                        )}
                    </div>
                </Link>
            </figure>

            <div className='flex gap-x-3 justify-between'>
                <div>
                    <h3 className='mb-1 font-bold text-base text-white line-clamp-1'>
                        {movie.title}
                    </h3>
                    <ul className='flex flex-col gap-y-1.5 text-sm leading-none font-medium'>
                        <li>{joinGenres(movie.genres)}</li>
                        <li className='text-accent'>{movie.country}</li>
                    </ul>
                </div>
                <div>
                    <WatchlistButton slug={movie.slug} is_watched={movie.is_watched} />
                </div>
            </div>
        </div>
    );
};
