import { cva, type VariantProps } from 'class-variance-authority';
import { type LucideIcon } from 'lucide-react';

import { cn } from '@/utils/helpers';

const badgeVariants = cva(
    'inline-flex items-center uppercase text-white px-1.5 py-1',
    {
        variants: {
            variant: {
                info: 'bg-info',
                secondary: 'bg-gray-900',
                primary: 'bg-primary',
            },
        },
        defaultVariants: {
            variant: 'primary',
        },
    },
);

interface BadgeProps
    extends React.BaseHTMLAttributes<HTMLDivElement>,
        VariantProps<typeof badgeVariants> {
    Icon?: LucideIcon;
}

export const Badge = ({
    className,
    Icon,
    variant,
    children,
    ...props
}: BadgeProps) => {
    return (
        <div className={cn(badgeVariants({ variant, className }))} {...props}>
            {Icon && <Icon size={14} />}
            <p className='leading-none font-bold text-xs'>{children}</p>
        </div>
    );
};
