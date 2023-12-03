import { Form, Field } from 'react-final-form';
import { useNavigate } from 'react-router-dom';

import { Button, Input } from '@/components';
import { routerMap } from '@/constants';
import { useRegisterMutation, type RegisterRequest } from '@/features/user';
import { getErrorMessage, composeValidators } from '@/utils/helpers';
import { required, minLength } from '@/utils/validators';

export const RegisterForm = () => {
    const [register, { isLoading, isError, error }] = useRegisterMutation();
    const navigate = useNavigate();
    const onSubmit = async (values: RegisterRequest) => {
        await register(values).unwrap();
        navigate(routerMap.sign_in);
    };
    return (
        <Form
            onSubmit={onSubmit}
            render={({ handleSubmit }) => (
                <form
                    className='flex flex-col gap-y-6 lg:gap-y-8'
                    onSubmit={handleSubmit}
                >
                    {isError && error && (
                        <div className='border-2 border-red-600 py-2'>
                            {getErrorMessage(error)}
                        </div>
                    )}
                    <Field
                        name='email'
                        id='registerEmail'
                        component={Input}
                        label='Имя пользователя'
                        type='email'
                        validate={required}
                    />
                    <Field
                        name='password'
                        id='registerPassword'
                        component={Input}
                        label='Пароль'
                        type='password'
                        validate={composeValidators(required, minLength(5))}
                    />
                    <Button
                        className='mt-2 w-full'
                        type='submit'
                        disabled={isLoading}
                    >
                        Зарегистрироваться
                    </Button>
                </form>
            )}
        />
    );
};
