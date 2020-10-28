import { TopicComponent } from './alltopics/topic/topic.component';
import { DeleteUserComponent } from './delete-user/delete-user.component';
import { PostComponent } from './alltopics/topic/post/post.component';
import { CommentComponent } from './alltopics/topic/post/comment/comment.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { AlltopicsComponent } from './alltopics/alltopics.component';
import { ProfileComponent } from './profile/profile.component';
import { ProfileSettingsComponent } from './profile-settings/profile-settings.component';

const routes: Routes = [
  //{ path: '', redirectTo: '/', pathMatch: 'full' },
  { path: 'login', component:LoginComponent},
  { path: 'signup', component:SignupComponent},
  { path: 'alltopics', component:AlltopicsComponent},
  //{ path: 'comment-test', component:CommentComponent},
  //{ path: 'post-test', component:PostComponent},
  { path: 'delete-user', component:DeleteUserComponent},
  { path: 'profile', component:ProfileComponent},
  { path: 'topic/:TopicName', component:TopicComponent},
  { path: 'settings', component:ProfileSettingsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
