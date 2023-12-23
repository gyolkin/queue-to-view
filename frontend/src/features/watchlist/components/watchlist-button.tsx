import { ListX, ListPlus } from "lucide-react";
import { useNavigate } from "react-router-dom";

import { routerMap } from "@/constants";
import { selectIsAuthenticated } from "@/features/user";
import { useWatchMovieMutation, useUnwatchMovieMutation } from '@/features/watchlist';
import { useAppSelector } from "@/hooks/store";

export const WatchlistButton = ({is_watched, slug}: {is_watched: boolean, slug: string}) => {
    const isAuthenticated = useAppSelector(selectIsAuthenticated);
    const navigate = useNavigate()
    const [watch] = useWatchMovieMutation();
    const [unwatch] = useUnwatchMovieMutation();
    const handleClick = async () => {
        if (isAuthenticated) {
            if (is_watched) {
                await unwatch(slug).unwrap();
            } else {
                await watch(slug).unwrap();
            }
        } else {
            navigate(routerMap.sign_in)
        }
    };
    return (
        <button onClick={handleClick}>
            {is_watched ?
                <ListX />
                : 
                <ListPlus />
            }
        </button>
    )
}
