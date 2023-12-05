import { Form, Field } from 'react-final-form';

import { Button, Input } from '@/components';
import { authApi, useLoginMutation, type LoginRequest } from '@/features/user';
import { getErrorMessage } from '@/utils/helpers';
import { required } from '@/utils/validators';

export const LoginForm = () => {
    const [login, { isLoading, isError, error }] = useLoginMutation();
    const [refetch] = authApi.endpoints.me.useLazyQuerySubscription();
    const onSubmit = async (values: LoginRequest) => {
        await login(values).unwrap();
        refetch();
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
                        id='loginEmail'
                        component={Input}
                        label='Имя пользователя'
                        type='email'
                        validate={required}
                    />
                    <Field
                        name='password'
                        id='loginPassword'
                        component={Input}
                        label='Пароль'
                        type='password'
                        validate={required}
                    />
                    <Button
                        className='mt-2 w-full'
                        type='submit'
                        disabled={isLoading}
                    >
                        Войти
                    </Button>
                </form>
            )}
        />
    );
};
