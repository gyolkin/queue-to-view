import { Button, Input } from '@/components';

export const RegisterForm = () => {
    return (
        <form className='flex flex-col gap-y-6 lg:gap-y-8'>
            <Input name='email' label='Ваш E-mail' />
            <Input name='password' label='Придумайте пароль' />
            <div className='mt-2'>
                <Button className='w-full'>Зарегистрироваться</Button>
            </div>
        </form>
    );
};
