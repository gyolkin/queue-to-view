import { Button, Input } from '@/components';

export const LoginForm = () => {
    return (
        <form className='flex flex-col gap-y-6 lg:gap-y-8'>
            <Input name='email' label='Ваш E-mail' />
            <Input name='password' label='Ваш пароль' />
            <div className='mt-2'>
                <Button className='w-full'>Войти</Button>
            </div>
        </form>
    );
};
