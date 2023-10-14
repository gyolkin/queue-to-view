import { useState, type FormEvent } from 'react';

import { useGetTestsQuery, useCreateTestMutation } from '@/features/test/api';
import { TestCard } from '@/features/test/components';

export const HomePage = () => {
    const [value, setValue] = useState<string>('Hello');
    const [createTest] = useCreateTestMutation();
    const { data, isLoading } = useGetTestsQuery();
    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();
        createTest(value);
    };
    if (isLoading || !data) {
        return <div>Данные загружаются...</div>;
    }
    return (
        <>
            <form method='POST' className='mb-4' onSubmit={handleSubmit}>
                <input
                    type='text'
                    value={value}
                    onChange={(e) => setValue(e.target.value)}
                />
                <button type='submit'>Create</button>
            </form>
            <div className='flex flex-row flex-wrap gap-4 max-w-7xl'>
                {data.map((item) => (
                    <TestCard key={item.id} {...item}></TestCard>
                ))}
            </div>
        </>
    );
};
