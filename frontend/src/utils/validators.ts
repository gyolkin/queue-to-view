import { FieldValidator } from 'final-form';

export type Validator = FieldValidator<string>;

export const required: Validator = (value) =>
    value ? undefined : 'Поле обязательно';

export const minLength =
    (min: number): Validator =>
    (value) =>
        value.trim().length >= min
            ? undefined
            : `Длина должна превышать ${min} символа`;
