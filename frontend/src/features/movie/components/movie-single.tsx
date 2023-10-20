import { Star, Timer } from 'lucide-react';
import { Link } from 'react-router-dom';

import { Badge } from '@/components';

export const MovieSingle = () => {
    return (
        <div className='col-span-full sm:col-span-6 lg:col-span-4 xl:col-span-3'>
            <figure className='mb-5'>
                <Link
                    className='group relative block h-full overflow-hidden bg-gray-900'
                    to='#'
                >
                    <img
                        className='aspect-[270/160] w-full object-cover transition-all duration-300 group-hover:scale-110 group-hover:opacity-75'
                        src='https://resizer.mail.ru/p/aa95b7bf-2e66-5c5c-9888-eca9bdbc554b/AAAC5OkXToR5d6NNua__shCRW0a9a_XLIX36GLY1rtdLUU1uPc37PTojIyoPVmUd5yYMpAg372kwWmUD4slKIgPPe-o.jpg'
                        alt='[XW] Shadow DLC Gameplay'
                    />
                    <div className='absolute inset-0 bg-black/60'></div>
                    <div className='absolute inline-flex gap-1 left-3.5 top-3'>
                        <Badge variant='primary' Icon={Timer}>
                            112
                        </Badge>
                        <Badge variant='info' Icon={Star}>
                            8.5
                        </Badge>
                    </div>
                </Link>
            </figure>

            <div className='flex gap-x-3'>
                <div className='shrink-0'>
                    <img
                        className='w-[40px]'
                        src='https://resizer.mail.ru/p/25e85ca5-28f1-5cd6-81e4-4bcc06c86650/AQAC90Ba1iwwb0luO4t9gN92bVMeFtKEL2TplUgfa0TIB3SvY_md4ZbcWNe2fevUoBuaEEovUTTz6h6_D-5v-THCUxU.webp'
                        alt=''
                    />
                </div>
                <div className='min-w-0'>
                    <h3 className='mb-1 font-bold text-base leading-tight text-white truncate w-full'>
                        1+1
                    </h3>
                    <ul className='flex flex-col gap-y-1.5 text-sm leading-none font-medium'>
                        <li>Драма</li>
                        <li className='text-accent'>Франция</li>
                    </ul>
                </div>
            </div>
        </div>
    );
};
