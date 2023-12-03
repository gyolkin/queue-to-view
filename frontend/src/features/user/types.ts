interface User {
    id: string;
    email: string;
    password: string;
    is_active: boolean;
    is_superuser: boolean;
    is_verified: boolean;
}

export interface ReadUser extends Readonly<Omit<User, 'password'>> {}
export interface LoginRequest extends Pick<User, 'email' | 'password'> {}
export interface RegisterRequest extends Pick<User, 'email' | 'password'> {}
