import { authApi } from '@/features/user';

export const ProfilePage = () => {
    const { data } = authApi.endpoints.me.useQueryState();
    return <div>{data?.email}</div>;
};
