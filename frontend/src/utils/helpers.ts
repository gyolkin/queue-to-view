import type { SerializedError } from '@reduxjs/toolkit';
import type { FetchBaseQueryError } from '@reduxjs/toolkit/query';
import { type ClassValue, clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

import { configMap } from '@/constants';
import type { ApiError } from '@/core/api';
import type { Validator } from '@/utils/validators';

const isApiError = (
    error: SerializedError | FetchBaseQueryError,
): error is ApiError => {
    return (
        typeof error === 'object' &&
        error != null &&
        'status' in error &&
        typeof error.status === 'number'
    );
};

export const composeValidators =
    (...validators: Array<Validator>): Validator =>
    (value, allValues, meta) =>
        validators.reduce(
            (error, validator) => error || validator(value, allValues, meta),
            undefined,
        );

export const cn = (...inputs: ClassValue[]) => {
    return twMerge(clsx(inputs));
};

export const getErrorMessage = (
    error: SerializedError | FetchBaseQueryError,
) => {
    if (isApiError(error)) {
        if (typeof error.data.detail === 'object') {
            return JSON.stringify(error.data.detail);
        } else {
            return error.data.detail;
        }
    } else {
        return configMap.unknown_error;
    }
};
