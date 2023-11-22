import type { FieldRenderProps } from 'react-final-form';

import { cn } from '@/utils/helpers';

interface InputProps extends FieldRenderProps<string, HTMLInputElement> {}

export const Input = ({ input, meta, label }: InputProps) => {
    const showError = meta.touched && (meta.error || meta.submitError);
    return (
        <div>
            <label
                className='block text-sm font-bold uppercase tracking-tight text-white'
                htmlFor={input.id}
            >
                {label}
            </label>
            <input
                {...input}
                className={cn(
                    'px-4 py-2 border-2 font-medium leading-8 tracking-tight transition-all duration-150 placeholder:font-normal focus:outline-0 focus:ring-0 text-white placeholder:text-gray-500/80 focus:border-accent focus:bg-gray-900 bg-gray-800 w-full',
                    showError ? 'border-red-600' : 'border-gray-600',
                )}
            />
            {showError && (
                <p className='text-red-500 text-sm mt-1'>
                    {meta.error || meta.submitError}
                </p>
            )}
        </div>
    );
};
