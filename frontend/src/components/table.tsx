import { cn } from '@/utils/helpers';

interface TableProps extends React.BaseHTMLAttributes<HTMLDListElement> {}
export const Table = ({ className, ...props }: TableProps) => {
    return (
        <dl
            className={cn(
                'grid grid-cols-8 gap-x-5 leading-normal md:gap-x-6 lg:gap-x-7.5',
                className,
            )}
            {...props}
        />
    );
};

interface TableRowProps {
    name: string;
    value: string | number;
}
export const TableRow = ({ name, value }: TableRowProps) => {
    return (
        <>
            <dt className='col-span-full text-gray sm:col-span-3'>{name}</dt>
            <dd className='col-span-full mb-4 font-bold text-white sm:col-span-5 md:mb-7'>
                {value}
            </dd>
        </>
    );
};
