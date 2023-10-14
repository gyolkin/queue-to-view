export const TestCard = ({ id, title }: { id: number; title: string }) => {
    return (
        <div className='p-5 border-r-teal-600 border-2'>
            <h2>Test #{id}</h2>
            <p>
                <strong>Title:</strong> {title}
            </p>
        </div>
    );
};
