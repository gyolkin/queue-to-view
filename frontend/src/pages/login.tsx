import { Heading } from '@/components';
import { LoginForm } from '@/features/user/components';

export const LoginPage = () => {
    return (
        <div className='flex flex-col gap-10 w-full mx-auto md:max-w-md md:pt-20'>
            <Heading>Авторизация</Heading>
            <LoginForm />
        </div>
    );
};
