import { Heading } from '@/components';
import { RegisterForm } from '@/features/user/components';

export const RegisterPage = () => {
    return (
        <div className='flex flex-col gap-10 w-full mx-auto md:max-w-md md:pt-20'>
            <Heading>Регистрация</Heading>
            <RegisterForm />
        </div>
    );
};
