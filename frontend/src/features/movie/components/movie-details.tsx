import { Table, TableRow, Heading } from '@/components';
import {
    joinGenres,
    transformDuration,
    type ReadMovie,
} from '@/features/movie';

export const MovieDetails = ({ movie }: { movie: ReadMovie }) => {
    return (
        <div className='grid grid-cols-12 gap-x-5 md:gap-x-6 lg:gap-x-7.5 gap-y-4'>
            <div className='col-span-full md:col-span-6 md:pr-7 lg:pr-[70px]'>
                <div className='sticky top-8'>
                    <div className='mb-9 aspect-[50/63] w-full'>
                        <img
                            className='h-full w-full object-cover'
                            src={movie.poster}
                            alt={movie.title}
                        />
                    </div>
                </div>
            </div>
            <div className='col-span-full md:col-span-6 lg:-ml-7.5'>
                <div className='mb-16 md:mb-20 lg:mb-24'>
                    <div className='flex justify-between items-baseline mb-5 lg:mb-8'>
                        <Heading size='sm'>{movie.title}</Heading>
                        {movie.imdb_rating && (
                            <Heading size='sm' variant='accent'>
                                IMDB: {movie.imdb_rating}
                            </Heading>
                        )}
                    </div>
                    <div className='mb-6 lg:mb-10'>{movie.description}</div>
                    <Table>
                        <TableRow name='Страна' value={movie.country} />
                        <TableRow
                            name='Год выпуска'
                            value={movie.release_year}
                        />
                        <TableRow
                            name='Жанры'
                            value={joinGenres(movie.genres)}
                        />
                        <TableRow
                            name='Длительность'
                            value={transformDuration(movie.duration)}
                        />
                    </Table>
                </div>
            </div>
        </div>
    );
};
