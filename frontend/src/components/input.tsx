interface InputProps {
    name: string;
    label: string;
}

export const Input = ({ name, label }: InputProps) => {
    return (
        <div>
            <label
                className='block text-sm font-bold uppercase tracking-tight text-white'
                htmlFor={name}
            >
                {label}
            </label>
            <input
                className='px-4 py-2 border-2 font-medium leading-8 tracking-tight transition-all duration-150 placeholder:font-normal focus:text-gray-900 focus:outline-0 focus:ring-0 border-gray-600 bg-gray-800 text-white placeholder:text-gray-500/80 focus:border-accent focus:bg-gray-900 w-full'
                type='email'
                name={name}
                id={name}
                value=''
                placeholder=''
            />
            {/* <p className="group-[.is-error]:block mt-2 hidden text-xs text-danger">
            </p> */}
        </div>
    );
};
