import React from 'react';

import { cva, type VariantProps } from 'class-variance-authority';

import { cn } from '@/utils/helpers';

const buttonVariants = cva('inline-flex justify-center', {
    variants: {
        shape: {
            default:
                'text-center font-bold leading-none transition-colors uppercase gap-x-3 py-4 px-4 md:py-[18px] lg:px-8 text-sm flex-1',
            rounded: 'items-center rounded-full',
        },
        variant: {
            accent: 'text-gray-900 bg-accent hover:bg-accent/90',
            secondary:
                'text-gray-500/40 ring-1 ring-inset ring-gray-500/40 bg-transparent hover:bg-accent hover:text-gray-900 hover:ring-0',
            primary: 'text-white bg-primary hover:bg-primary/90',
        },
    },
    defaultVariants: {
        shape: 'default',
        variant: 'accent',
    },
});

interface ButtonProps
    extends React.ButtonHTMLAttributes<HTMLButtonElement>,
        VariantProps<typeof buttonVariants> {}

export const Button = ({
    className,
    variant,
    shape,
    ...props
}: ButtonProps) => {
    return (
        <button
            className={cn(buttonVariants({ shape, variant, className }))}
            {...props}
        />
    );
};
