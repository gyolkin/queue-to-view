import { Shuffle } from 'lucide-react';

import { Button, Heading } from '@/components';
import { textMap } from '@/constants';

export const RandomMovie = () => {
    const { random_movie } = textMap.features;

    return (
        <div className='grid grid-cols-12 gap-x-5 gap-y-5 lg:gap-y-12 md:gap-x-6 lg:gap-x-7.5'>
            <div className='col-span-full grid grid-cols-7 gap-x-5 sm:grid-rows-[197px_107px_85px] md:col-span-7 md:grid-rows-[152px_83px_66px] md:gap-x-6 lg:grid-rows-[197px_107px_85px] lg:gap-x-7.5 xl:grid-rows-[246px_134px_106px]'>
                <figure className='col-span-full sm:row-start-1 sm:row-end-3'>
                    <img
                        className='w-full sm:w-auto md:w-[640px]'
                        src='https://resizer.mail.ru/p/aa95b7bf-2e66-5c5c-9888-eca9bdbc554b/AAAC5OkXToR5d6NNua__shCRW0a9a_XLIX36GLY1rtdLUU1uPc37PTojIyoPVmUd5yYMpAg372kwWmUD4slKIgPPe-o.jpg'
                        alt=''
                    />
                </figure>
                <figure className='relative hidden sm:block col-span-full sm:col-span-5 sm:col-start-2 sm:row-start-2 sm:row-end-4 sm:pl-3 sm:pr-10'>
                    <img
                        className='h-full sm:w-auto sm:shadow-[0_0_60px_0_rgba(0,0,0,.4)]'
                        src='https://resizer.mail.ru/p/25e85ca5-28f1-5cd6-81e4-4bcc06c86650/AQAC90Ba1iwwb0luO4t9gN92bVMeFtKEL2TplUgfa0TIB3SvY_md4ZbcWNe2fevUoBuaEEovUTTz6h6_D-5v-THCUxU.webp'
                        alt=''
                    />
                    <Button
                        shape='rounded'
                        variant='primary'
                        className='absolute -left-12 top-3/4 hidden aspect-square w-20 -translate-y-2/3 sm:flex shadow-[0_0_60px_0_rgba(0,0,0,.4)]'
                    >
                        <Shuffle />
                    </Button>
                </figure>
                <div className='relative col-span-full sm:col-span-2 sm:col-start-4 sm:row-start-3 sm:row-end-4 sm:pl-3 sm:pr-10'>
                    <Button>{random_movie.gen_button_details}</Button>
                </div>
            </div>
            <div className='col-span-full md:col-span-5'>
                <div className='md:-ml-[56px] lg:-ml-[80px] xl:-ml-[110px]'>
                    <Heading className='mb-2 lg:mb-6'>
                        {random_movie.gen_heading1}
                    </Heading>
                    <Heading size='md' variant='accent'>
                        1+1
                    </Heading>
                </div>
                <div className='md:pl-4 md:pr-2 lg:px-7 xl:pr-[70px] xl:pl-10 [&_p]:mb-8'>
                    <p>
                        Богатый бизнесмен Филипп становится инвалидом по вине
                        несчастного случая (прототип героя — французский
                        аристократ Филиппа Поццо ди Борго). Помогая бедняге
                        адаптироваться, врачи направляют к нему работников по
                        уходу за больными. Из всех кандидатов на роль медбрата
                        привередливый богач выбирает самого странного: молодого
                        африканского эмигранта с судимостью. Непосредственный
                        араб становится для скучающего Филиппа и
                        ангелом-хранителем, и источником ежедневных приключений.
                        Отношения двух мужчин из разных социальных слоев
                        перерастают в крепкую дружбу.
                    </p>
                </div>
            </div>
        </div>
    );
};
