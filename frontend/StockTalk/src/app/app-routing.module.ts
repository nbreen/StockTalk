import { SuggestionsComponent } from './suggestions/suggestions.component';
import { ViewSinglePostComponent } from './view-single-post/view-single-post.component';
import { ViewSavedPostsComponent } from './view-saved-posts/view-saved-posts.component';
import { FollowersComponent } from './followers/followers.component';
import { TopicComponent } from './alltopics/topic/topic.component';
import { DeleteUserComponent } from './delete-user/delete-user.component';
import { PostComponent } from './alltopics/topic/post/post.component';
import { CommentComponent } from './alltopics/topic/post/comment/comment.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { AlltopicsComponent } from './alltopics/alltopics.component';
import { TrendingtopicsComponent } from './trendingtopics/trendingtopics.component';
import { ProfileComponent } from './profile/profile.component';
import { ProfileSettingsComponent } from './profile-settings/profile-settings.component';
import { MakePostComponent } from './make-post/make-post.component';
import { VerifyComponent } from './verify/verify.component';
import { HomepageComponent } from './homepage/homepage.component';

const routes: Routes = [
  //{ path: '', redirectTo: '/', pathMatch: 'full' },
  { path: 'login', component:LoginComponent},
  { path: 'signup', component:SignupComponent},
  { path: 'alltopics', component:AlltopicsComponent},
  //{ path: 'comment-test', component:CommentComponent},
  //{ path: 'post-test', component:PostComponent},
  { path: 'delete-user', component:DeleteUserComponent},
  { path: 'profile/:User', component:ProfileComponent},
  { path: 'topic/:TopicName', component:TopicComponent},
  { path: 'settings/:User', component: ProfileSettingsComponent },
  { path: 'trendingtopics', component: TrendingtopicsComponent },
  { path: 'followers/:User', component: FollowersComponent},
  { path: 'makepost/:User', component: MakePostComponent },
  { path: 'post/:PostId', component: ViewSinglePostComponent },
  { path: 'mysavedposts', component : ViewSavedPostsComponent },
  { path: 'suggestions', component : SuggestionsComponent},
  { path: 'verify', component: VerifyComponent},
  { path: 'homepage/:User', component: HomepageComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
