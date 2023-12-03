import { cva, type VariantProps } from 'class-variance-authority';

import { cn } from '@/utils/helpers';

const alertVariants = cva('border-l-4 p-4', {
    variants: {
        variant: {
            // info: 'bg-info-1/4 border-info',
            // success: 'bg-accent-1/4 border-accent',
            fail: 'bg-red-200 border-red-500 text-red-700',
        },
    },
    defaultVariants: {
        variant: 'fail',
    },
});

interface AlertProps
    extends React.BaseHTMLAttributes<HTMLDivElement>,
        VariantProps<typeof alertVariants> {}

export const Alert = ({
    className,
    variant,
    children,
    ...props
}: AlertProps) => {
    return (
        <div
            className={cn(alertVariants({ variant, className }))}
            {...props}
            role='alert'
        >
            <p>{children}</p>
        </div>
    );
};
