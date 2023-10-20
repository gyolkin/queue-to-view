import { cva, type VariantProps } from 'class-variance-authority';
import { Link, NavLink, type LinkProps } from 'react-router-dom';

import { cn } from '@/utils/helpers';

export const NavbarLink = ({
    to,
    children,
    className,
    ...props
}: LinkProps) => {
    return (
        <NavLink
            to={to}
            className={({ isActive }) =>
                cn(
                    'group relative inline-flex items-center gap-x-3 leading-10 px-3.5 xl:px-4.5 after:absolute after:top-[15px] after:left-0 after:transition-transform after:w-1.5 after:h-[9px] after:bg-current-marker',
                    isActive
                        ? 'after:origin-left after:scale-x-100'
                        : 'after:origin-right hover:after:origin-left after:scale-x-0 hover:after:scale-x-100',
                    className,
                )
            }
            {...props}
        >
            {children}
        </NavLink>
    );
};

const defaultLinkVariants = cva('inline-flex items-center', {
    variants: {
        variant: {
            default:
                'justify-between py-1.5 transition-colors hover:text-accent',
            dropdown:
                'group relative gap-x-3 leading-10 px-3.5 xl:px-4.5 after:absolute after:top-[15px] after:left-0 after:transition-transform after:w-1.5 after:h-[9px] after:bg-current-marker after:origin-right hover:after:origin-left after:scale-x-0 hover:after:scale-x-100',
            link: 'text-center font-bold leading-none transition-colors uppercase justify-center gap-x-3 py-4 px-4 md:py-[18px] lg:px-8 text-sm flex-1 text-gray-900 bg-accent hover:bg-accent/90',
        },
    },
    defaultVariants: {
        variant: 'default',
    },
});

interface DefaultLinkProps
    extends LinkProps,
        VariantProps<typeof defaultLinkVariants> {}

export const DefaultLink = ({
    to,
    variant,
    className,
    children,
    ...props
}: DefaultLinkProps) => {
    return (
        <Link
            to={to}
            className={cn(defaultLinkVariants({ variant, className }))}
            {...props}
        >
            {children}
        </Link>
    );
};
