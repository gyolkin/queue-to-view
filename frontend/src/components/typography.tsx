import React from 'react';

import { cva, type VariantProps } from 'class-variance-authority';

import { cn } from '@/utils/helpers';

const headingVariants = cva(
    'font-bold tracking-tighter md:-mt-[0.6em] md:leading-none',
    {
        variants: {
            size: {
                sm: 'text-xl lg:text-2xl',
                md: 'text-2xl lg:text-4xl',
                lg: 'text-4xl lg:text-6xl',
                xl: 'text-6xl lg:text-8xl',
            },
            variant: {
                white: 'text-white',
                accent: 'text-accent',
            },
        },
        defaultVariants: {
            size: 'lg',
            variant: 'white',
        },
    },
);

interface HeadingProps
    extends React.BaseHTMLAttributes<HTMLHeadingElement>,
        VariantProps<typeof headingVariants> {}

export const Heading = ({
    variant,
    size,
    className,
    ...props
}: HeadingProps) => {
    return (
        <h1
            className={cn(headingVariants({ variant, size, className }))}
            {...props}
        />
    );
};
