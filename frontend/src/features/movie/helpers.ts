import type { ReadGenre } from '@/features/genre';

export const joinGenres = (genres: Array<ReadGenre>): string => {
    return genres.map((genre) => genre.title).join(', ');
};

export const transformDuration = (duration: number): string => {
    const hours = Math.floor(duration / 60);
    const remainingMinutes = duration % 60;
    const formattedHours = hours.toString().padStart(2, '0');
    const formattedMinutes = remainingMinutes.toString().padStart(2, '0');
    return `${duration} мин. / ${formattedHours}:${formattedMinutes}`;
};
